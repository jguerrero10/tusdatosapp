from alembic.config import CommandLine, Config

from config import settings


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
    CommandLine().main(argv=["upgrade", "head"])

if __name__ == "__main__":
    run_migrations()
