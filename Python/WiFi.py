import subprocess

def get_wifi_profiles():
    """
    Retrieve the list of saved Wi-Fi profiles on a Windows system.
    """
    try:
        # Run 'netsh wlan show profiles' command to get the list of profiles
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], 
                                 capture_output=True, text=True, encoding='utf-8')
        profiles = result.stdout.split('\n')

        # Filter and extract Wi-Fi profile names
        wifi_profiles = []
        for line in profiles:
            if 'All User Profile     : ' in line:
                wifi_profiles.append(line.split(': ')[1].strip())

        return wifi_profiles
    except Exception as e:
        print(f"Error retrieving Wi-Fi profiles: {e}")
        return []

def extract_password(profile_name):
    """
    Extract the password for the given Wi-Fi profile.
    """
    try:
        # Run 'netsh wlan show profile name=<profile_name> key=clear' to get profile details
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', 
                                 f'name={profile_name}', 'key=clear'], 
                                 capture_output=True, text=True, encoding='utf-8')
        lines = result.stdout.split('\n')

        # Look for the line containing 'Key Content' for the password
        for line in lines:
            if 'Key Content            : ' in line:
                return line.split(': ')[1].strip()

        return '<No Password>'
    except Exception as e:
        print(f"Error extracting password for {profile_name}: {e}")
        return '<No Password>'

def get_nearby_networks():
    """
    Retrieve the list of nearby Wi-Fi networks (hotspots) in range.
    """
    try:
        # Run 'netsh wlan show networks mode=bssid' command to get networks in range
        result = subprocess.run(['netsh', 'wlan', 'show', 'networks', 'mode=bssid'], 
                                 capture_output=True, text=True, encoding='utf-8')
        networks = result.stdout.split('\n')

        # Extract network names (SSIDs)
        nearby_networks = []
        for line in networks:
            if 'SSID ' in line and 'BSSID' not in line:
                ssid = line.split(': ')[1].strip()
                if ssid:  # Ensure SSID is not empty
                    nearby_networks.append(ssid)

        return nearby_networks
    except Exception as e:
        print(f"Error retrieving nearby networks: {e}")
        return []

def main():
    """
    Main function to retrieve and display Wi-Fi profiles, passwords, and nearby hotspots.
    """
    # Retrieve Wi-Fi profiles
    wifi_profiles = get_wifi_profiles()

    # Display saved Wi-Fi profiles and their passwords
    print("Saved Wi-Fi Profiles:")
    print("Wi-Fi Name                Password")
    print("---------------------------------")
    for profile_name in wifi_profiles:
        password = extract_password(profile_name)
        print(f"{profile_name:<20} {password}")

    # Retrieve and display nearby Wi-Fi networks
    print("\nNearby Wi-Fi Networks:")
    print("Wi-Fi Name")
    print("----------")
    nearby_networks = get_nearby_networks()
    for network in nearby_networks:
        print(network)

if __name__ == "__main__":
    main()