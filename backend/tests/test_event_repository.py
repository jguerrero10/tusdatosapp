from core.entities.event import EventCreate, EventUpdate


def test_create_event(event_repository):
    event = EventCreate(
        name="Test Repo Event",
        description="Repo test",
        capacity=100,
        start_date="2025-09-01T10:00:00",
        end_date="2025-09-01T12:00:00",
        state=True,
    )
    created = event_repository.create_event(event)
    assert created.id is not None
    assert created.name == "Test Repo Event"
    assert created.state is True


def test_get_events(event_repository):
    all_events = event_repository.get_events()
    assert isinstance(all_events, list)
    assert len(all_events) >= 1


def test_get_event_by_id(event_repository):
    event = EventCreate(
        name="Lookup Event",
        description="Find me",
        capacity=10,
        start_date="2025-09-02T09:00:00",
        end_date="2025-09-02T11:00:00",
        state=True,
    )
    created = event_repository.create_event(event)
    found = event_repository.get_event_by_id(created.id)
    assert found is not None
    assert found.name == "Lookup Event"


def test_get_event_by_id_not_found(event_repository):
    event = event_repository.get_event_by_id(999999)
    assert event is None


def test_search_events(event_repository):
    event = EventCreate(
        name="Unique Search Term",
        description="Searchable",
        capacity=50,
        start_date="2025-09-03T14:00:00",
        end_date="2025-09-03T16:00:00",
        state=True,
    )
    event_repository.create_event(event)
    results = event_repository.search_events("Unique")
    assert any("Unique" in e.name for e in results)


def test_update_event(event_repository):
    event = EventCreate(
        name="Updatable Event",
        description="Before update",
        capacity=30,
        start_date="2025-09-04T10:00:00",
        end_date="2025-09-04T12:00:00",
        state=True,
    )
    created = event_repository.create_event(event)
    updated = event_repository.update_event(created.id, EventUpdate(description="After update", capacity=40))
    assert updated.description == "After update"
    assert updated.capacity == 40


def test_update_event_not_found(event_repository):
    result = event_repository.update_event(event_id=99999, event=EventUpdate(description="Does not exist"))
    assert result is None


def test_inactivate_event(event_repository):
    event = EventCreate(
        name="Inactivable",
        description="To be inactivated",
        capacity=25,
        start_date="2025-09-05T09:00:00",
        end_date="2025-09-05T10:00:00",
        state=True,
    )
    created = event_repository.create_event(event)
    result = event_repository.inactivate_event(created.id)
    assert result.state is False
