class EmailAddress:
    def __init__(self, address: str):
        if self.__check_correct_address(address):
            self._address = address
        else:
            raise ValueError()

    @property
    def address(self) -> str:
        return self.__normalize_address(self._address)

    @property
    def masked(self) -> str:
        login, domain = self.__extract_login_domain(self.address)
        return f"{login[:2]}***@{domain}"

    @staticmethod
    def __normalize_address(email: str) -> str:
        return email.strip().lower()

    @staticmethod
    def __check_correct_address(address: str) -> bool:
        return "@" in address and any(domain in address.lower() for domain in ('.com', '.ru', '.net'))

    @staticmethod
    def __extract_login_domain(address: str) -> tuple[str, str]:
        login, domain = address.split("@")
        return login, domain
