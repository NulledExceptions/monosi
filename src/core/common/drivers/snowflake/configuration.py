from dataclasses import dataclass

from core.common.drivers.base import BaseDriverConfiguration

@dataclass
class SnowflakeDriverConfiguration(BaseDriverConfiguration):
    user: str
    password: str
    warehouse: str
    database: str
    account: str

    def driver_name(self):
        return "snowflake"

    def configuration_schema(self):
        return {}

    def connection_string(self) -> str:
        return 'snowflake://{user}:{password}@{account}/'.format(
            user=self.user,
            password=self.password,
            account=self.account,
        )

    @classmethod
    def from_dict(cls, config_dict):
        return cls(
            user=config_dict.get('user'),
            password=config_dict.get('password'),
            warehouse=config_dict.get('warehouse'),
            database=config_dict.get('database'),
            account=config_dict.get('account'),
        )

    def to_dict(self):
        return {
            'user': self.user,
            'warehouse': self.warehouse,
            'database': self.database,
            'account': self.account,
        }
    