from pydantic import BaseModel, field_validator, computed_field, model_validator, Field
from typing import Optional

class BookTicket(BaseModel):
    pnr: str
    name: str = Field(
        ...,
        min_length=3
    )
    email: str = Field(
      ...,
      pattern=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"  
    )
    no_of_adults: int
    no_of_childs: int
    child_age: int
    seating_info: str
    booking_status: str
    travel_insurance: Optional[bool] = False
    total_distance: int
    price_per_km: float
    
    @computed_field
    @property
    def calculate_ticket_price(self) -> float:
        return self.total_distance * self.price_per_km
    
    @computed_field
    @property
    def format_seating_info(self) -> list[str]:
        return self.seating_info.strip().split(',')
    
    @model_validator(mode="before")
    def validateAdultAndChild(cls, values):
        no_of_childs = values.get("no_of_childs")
        no_of_adults = values.get("no_of_adults")
        child_age = values.get("child_age")

        if child_age > 7:
            raise ValueError("Child age is not acceptable. Book an extra ticket")

        if no_of_adults == 0 and no_of_childs == 0:
            raise ValueError("At least one adult or child needed")

        return values

booking_ticket = {
    "pnr": "689097547",
    "name": "Peti",
    "email": "peti789@gmail.com",
    "no_of_adults": 4,
    "no_of_childs": 1,
    "child_age": 10,
    "seating_info": "SU-67-B2,LB-68-B2,MB-66-B2",
    "booking_status": "CNF",
    "travel_insurance": True,
    "total_distance": 1600,
    "price_per_km": 1.5
}

# ticket_price = {
#     "payment_mode": "UPI",
# }

bookTicketModel = BookTicket(**booking_ticket)
# print(bookTicketModel.calculate_ticket_price)
# print(bookTicketModel.format_seating_info)
# print(bookTicketModel.validateAdultAndChild)