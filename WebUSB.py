import streamlit as st
import streamlit.components.v1 as components

st.title("Arduino LED Control via WebUSB")

# Embed the HTML and JavaScript for WebUSB
html_code = """
<!DOCTYPE html>
<html>
  <head>
    <title>WebUSB Arduino LED Control</title>
  </head>
  <body>
    <h1>WebUSB Arduino LED Control</h1>
    <button id="connectButton">Connect to Arduino</button>
    <button id="ledOnButton">Turn LED On</button>
    <button id="ledOffButton">Turn LED Off</button>
    <script>
      let device;

      document.getElementById('connectButton').addEventListener('click', async () => {
        try {
          device = await navigator.usb.requestDevice({ filters: [{ vendorId: 0x2341 }] });
          await device.open();
          await device.selectConfiguration(1);
          await device.claimInterface(2);
          console.log('Connected to Arduino');
        } catch (error) {
          console.error('There was an error:', error);
        }
      });

      document.getElementById('ledOnButton').addEventListener('click', async () => {
        if (device) {
          const encoder = new TextEncoder();
          const data = encoder.encode('1');
          await device.transferOut(4, data);
          console.log('LED On');
        }
      });

      document.getElementById('ledOffButton').addEventListener('click', async () => {
        if (device) {
          const encoder = new TextEncoder();
          const data = encoder.encode('0');
          await device.transferOut(4, data);
          console.log('LED Off');
        }
      });
    </script>
  </body>
</html>
"""

components.html(html_code)
