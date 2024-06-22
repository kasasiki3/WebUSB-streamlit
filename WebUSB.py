import streamlit as st
import streamlit.components.v1 as components

st.title("WebUSB LED Control")

components.html("""
<!DOCTYPE html>
<html>
<body>
  <button onclick="connectDevice()">Connect to Arduino</button>
  <button onclick="sendCommand('ON')">Turn LED On</button>
  <button onclick="sendCommand('OFF')">Turn LED Off</button>
  <p id="status">Status: Disconnected</p>

  <script>
    let device;

    async function connectDevice() {
      try {
        device = await navigator.usb.requestDevice({ filters: [{ vendorId: 0x0f0d }] });
        await device.open();
        await device.selectConfiguration(1);
        await device.claimInterface(0);
        document.getElementById('status').innerText = "Status: Connected";
      } catch (error) {
        console.log(error);
        document.getElementById('status').innerText = "Status: Error connecting to device";
      }
    }

    async function sendCommand(command) {
      if (!device) {
        alert("Device not connected");
        return;
      }

      const encoder = new TextEncoder();
      const data = encoder.encode(command + "\n");

      try {
        await device.transferOut(2, data);
        console.log("Sent: " + command);
      } catch (error) {
        console.log(error);
      }
    }
  </script>
</body>
</html>
""", height=300)
