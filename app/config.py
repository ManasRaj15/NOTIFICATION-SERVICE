from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    EMAIL_FROM: str
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_HOST: str
    EMAIL_PORT: int

    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_PHONE_NUMBER: str

    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()