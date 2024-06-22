import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html>
  <head>
    <title>WebUSB LED Control</title>
    <script>
      let device;

      async function connect() {
        try {
          device = await navigator.usb.requestDevice({ filters: [{ vendorId: 0x2341 }] });
          await device.open();
          await device.selectConfiguration(1);
          await device.claimInterface(0);  // インターフェイス番号0を使用
          console.log('Connected to device');
        } catch (error) {
          console.log('There was an error: ' + error);
        }
      }

      async function toggleLED(state) {
        try {
          const data = new Uint8Array([state]);
          await device.transferOut(4, data);  // エンドポイント4を使用
          console.log('LED state set to ' + state);
        } catch (error) {
          console.log('There was an error: ' + error);
        }
      }
    </script>
  </head>
  <body>
    <button onclick="connect()">Connect</button>
    <button onclick="toggleLED(1)">Turn LED ON</button>
    <button onclick="toggleLED(0)">Turn LED OFF</button>
  </body>
</html>
"""

components.html(html_code)
