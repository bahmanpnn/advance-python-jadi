from datetime import datetime
# from dateutil.relativedelta import relativedelta  # pip install python-dateutil


class UserDate:
    def __init__(self, date_str):
        self.date_str = date_str
        self.birth_date = self.validate_date()  # Validate the input date when creating an instance

    def validate_date(self):
        """Check if the input date is valid or not"""
        try:
            return datetime.strptime(self.date_str, "%Y/%m/%d")  # Convert the input string to datetime
        except ValueError:
            return "wrong"  # Return 'wrong' if the input format is incorrect

    def calculate_age(self):
        """Calculate the age if the date is valid"""
        if self.birth_date == "wrong":
            return "wrong"  # If the date is invalid, return 'wrong'
        
        current_date = datetime.now()

        # Calculate the approximate age using days difference

        # age = relativedelta(current_date, self.birth_date)
        age = int((current_date - self.birth_date).days / 365)
        
        # return f"{age:.2f} years"  # Format age to 2 decimal places
        return f"you are {age} year/years old"



def main():
    
    # Get input from the user
    user_input = input("Enter your birthdate (YYYY/MM/DD): ")

    # Create an instance of UserDate
    user_date = UserDate(user_input)

    # Show output and result
    if user_date.birth_date == "wrong":
        print("wrong")  # Invalid date format
    else:
        print(user_date.calculate_age())  # Display the calculated age


if __name__ == "__main__":
    main()


