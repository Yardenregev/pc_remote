# 📱💻 PC Remote Controller

Control your PC from your phone like a remote! This project is a Django-based application that allows you to manage various PC functions remotely using your mobile device.

## 🚀 Features
*   Move your mouse through the trackpad and tap to click
*   Use your mobile keyboard to type keyboard inputs
*   Raise and lower volume
*   Scroll pages
*   Press important buttons such as 'Delete', 'Backspace', 'Enter' and more...
  
## ⚠️ Disclaimer
This project was only tested on Windows 11.  Compatibility with other operating systems is not guaranteed.

## ⚙️ Prerequisites
* Python **Over 3.7, Under 3.12**

## 🛠️ Installation
1.  Open Command Prompt or Windows PowerShell
2.  Clone the GitHub repository:
   ```sh
git clone https://github.com/Yardenregev/pc_remote_controller.git
```
3. Navigate to the project directory:
```sh
cd pc_remote_controller
```
4.  Run the installation script:
   ```sh
   .\install.bat
   ```
5.  Follow the on-screen instructions during the installation process.
    1. The username and password you have entered when creating the user in the installation process will be the credentials you will need to use when logging in.

## 🏃‍♂️ Running the Application
1.  Run the launch script:
   ```sh
   .\launch.bat
   ```
2.  (Optional) Create a desktop shortcut for `launch.bat` for easier access.

## 📱 Accessing the Application from Your Phone
Once the application is running, you can access it from your phone's web browser.
The `launch.bat` script will display 3 potential URLs in cyan:

*   `https://<hostname>:8443`
*   `https://<hostname>.local:8443`
*   `https://<your_ip_address>:8443`

One of these should work. The `.local` address is often easier for devices on the same local network to resolve.

**Note:** On the first time you try to access the application you will see a "Connection is not private message" (since it is encrypted through a Self Signed Certificate). You should click on "Show details" -> "visit this website" -> "visit website".

**Creating a Home Screen Shortcut on your phone (Optional):**

Once you have a working URL, you can create a shortcut to it on your phone's home screen for quick access.


## 🔒 Security
*   Communication is encrypted using a self-signed certificate.
*   User login is encrypted.
*   Login attempts are rate-limited to 5 attempts to prevent brute-force attacks.

## 📓 Additional Notes
**Hostname vs. IP Address:**
The hostname option (`https://<hostname>:8443`) relies on your network's ability to resolve the hostname to the IP address of your PC, allowing for a relatively consistant URL to access the platform.
While it can work in some mobile browsers such as Safari, some other browsers such as Chrome often restrict access to servers using hostnames due to security policies related to mixed content or local network access restrictions.
They may require a more explicit user confirmation or configuration, therefore you will need to use the ip address option when using one of these browsers.



**Important Note about IP Addresses:** 
Your local IP address might change when you disconnect and reconnect to your network or when your router assigns a new DHCP lease. This means bookmarks or home screen shortcuts using the IP address might break. You'll need to update the shortcut with the new IP address if it changes.  A static local IP address configuration on your router can mitigate this issue.