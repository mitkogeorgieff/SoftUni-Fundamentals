import re

pattern = r"(@[#]+)([A-Z]([a-zA-Z0-9]{4,})[A-Z])(@[#]+)"
digits_group = r"\d"

# Get the number of barcodes from the user
number_barcodes = int(input())

# Loop through each barcode and extract the product group number
for _ in range(number_barcodes):
    # Get the barcode from the user
    barcode = input()

    # If the barcode matches the pattern, extract the product group number
    if re.match(pattern, barcode):
        # Find all digit characters in the barcode
        digits = re.findall(digits_group, barcode)

        # If there are digit characters in the barcode, concatenate them to form the product group number
        if digits:
            product_group = ''.join(digits)
        else:
            # If there are no digit characters in the barcode, set the product group number to "00"
            product_group = '00'

        # Print the product group number
        print(f"Product group: {product_group}")

    # If the barcode does not match the pattern, print an error message
    else:
        print("Invalid barcode")
