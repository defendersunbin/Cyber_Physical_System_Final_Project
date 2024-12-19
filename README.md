# Cyber_Physical_System_Final_Project
 Simulation of smart factory recovering from DoS attack

 ![download](https://github.com/user-attachments/assets/7454e66d-8f5c-498a-8e1b-5573e6a6e131)

Here are the results

```
[INFO] Starting CPS simulation...
Step 1: Total Traffic Load = 52, Temperature = 25.20°C, HVAC State = OFF
Step 2: Total Traffic Load = 114, Temperature = 36.60°C, HVAC State = ON
Step 3: Total Traffic Load = 159, Temperature = 52.00°C, HVAC State = ON
Step 4: Total Traffic Load = 221, Temperature = 73.60°C, HVAC State = ON
Step 5: Total Traffic Load = 286, Temperature = 101.70°C, HVAC State = ON
Step 6: Total Traffic Load = 328, Temperature = 134.00°C, HVAC State = ON
Step 7: Total Traffic Load = 384, Temperature = 171.90°C, HVAC State = ON
Step 8: Total Traffic Load = 437, Temperature = 215.10°C, HVAC State = ON
Step 9: Total Traffic Load = 482, Temperature = 262.80°C, HVAC State = ON
Step 10: Total Traffic Load = 527, Temperature = 315.00°C, HVAC State = ON

[ALERT] Simulating DoS attack on Nodes [3, 5, 7]
  - Node 3 traffic increased to 181
  - Node 5 traffic increased to 135
  - Node 7 traffic increased to 152
  - Node 3 traffic increased to 325
  - Node 5 traffic increased to 213
  - Node 7 traffic increased to 208
  - Node 3 traffic increased to 404
  - Node 5 traffic increased to 299
  - Node 7 traffic increased to 310
  - Node 3 traffic increased to 520
  - Node 5 traffic increased to 436
  - Node 7 traffic increased to 402
  - Node 3 traffic increased to 635
  - Node 5 traffic increased to 515
  - Node 7 traffic increased to 471

[INFO] Attack Complete. Monitoring System Recovery...
  Recovery Step 1: {3: {'traffic': 563, 'cpu_usage': 56.3, 'memory_load': 28.15}, 5: {'traffic': 435, 'cpu_usage': 43.5, 'memory_load': 21.75}, 7: {'traffic': 401, 'cpu_usage': 40.1, 'memory_load': 20.05}}
  Recovery Step 2: {3: {'traffic': 497, 'cpu_usage': 49.699999999999996, 'memory_load': 24.849999999999998}, 5: {'traffic': 373, 'cpu_usage': 37.3, 'memory_load': 18.65}, 7: {'traffic': 319, 'cpu_usage': 31.9, 'memory_load': 15.95}}
  Recovery Step 3: {3: {'traffic': 424, 'cpu_usage': 42.4, 'memory_load': 21.2}, 5: {'traffic': 278, 'cpu_usage': 27.799999999999997, 'memory_load': 13.899999999999999}, 7: {'traffic': 255, 'cpu_usage': 25.5, 'memory_load': 12.75}}
  Recovery Step 4: {3: {'traffic': 336, 'cpu_usage': 33.6, 'memory_load': 16.8}, 5: {'traffic': 195, 'cpu_usage': 19.499999999999996, 'memory_load': 9.749999999999998}, 7: {'traffic': 195, 'cpu_usage': 19.5, 'memory_load': 9.75}}
  Recovery Step 5: {3: {'traffic': 257, 'cpu_usage': 25.700000000000003, 'memory_load': 12.850000000000001}, 5: {'traffic': 130, 'cpu_usage': 12.999999999999996, 'memory_load': 6.499999999999998}, 7: {'traffic': 111, 'cpu_usage': 11.100000000000001, 'memory_load': 5.550000000000001}}
[INFO] System recovered successfully.


[INFO] Service Availability: 0.00%
[INFO] Average Recovery Time: 3.00 steps
```
