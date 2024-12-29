import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from geopy.geocoders import Nominatim

# Set up Twilio client
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(to, body):
    try:
        message = client.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=to
        )
        print(f"Sent message with SID: {message.sid}")
    except TwilioRestException as e:
        print(f"Failed to send message: {e}")

# Function to geolocate IP address
def geolocate_ip(ip_address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ip_address)
    if location:
        return location.address
    else:
        return "Location not found"

# Main function
def main():
    mobile_number = '8275268881'
    tracking_link = 'https://grabify.link/your_tracking_link'

    # Send SMS with tracking link
    send_sms(mobile_number, tracking_link)

    # Wait for the target to click the link (you may need to implement a delay or polling mechanism)
    # For demonstration purposes, we'll assume you have obtained the IP address
    ip_address = '192.168.1.1'  # Replace with the actual IP address obtained from Grabify

    # Geolocate the IP address
    location = geolocate_ip(ip_address)
    print(f"Location: {location}")

if __name__ == "__main__":
    main()