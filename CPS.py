import random
import matplotlib.pyplot as plt
import numpy as np

# 보완된 네트워크 노드 클래스
class Node:
    def __init__(self, id, bandwidth, latency):
        self.id = id
        self.bandwidth = bandwidth
        self.latency = latency
        self.capacity = random.randint(200, 300)  # 각 노드의 처리 용량을 더욱 증가
        self.traffic = 0
        self.cpu_usage = 0
        self.memory_load = 0
        self.attack_detected = False

    def send_traffic(self, amount):
        if not self.attack_detected:  # 공격 탐지 시 트래픽 차단
            self.traffic += amount
            self.cpu_usage = min(100, self.cpu_usage + amount * 0.1)
            self.memory_load = min(100, self.memory_load + amount * 0.05)

    def receive_traffic(self, amount):
        self.traffic = max(0, self.traffic - amount)
        self.cpu_usage = max(0, self.cpu_usage - amount * 0.1)
        self.memory_load = max(0, self.memory_load - amount * 0.05)

    def is_overloaded(self):
        return self.cpu_usage >= 80  # CPU 사용량이 80%를 초과하면 과부하로 간주

    def detect_attack(self):
        # 공격 탐지 알고리즘
        if self.traffic > self.capacity * 0.8:
            self.attack_detected = True
            print(f"[ALERT] Attack detected on Node {self.id} with traffic {self.traffic}")

    def recover(self):
        # 공격 복구 로직
        if self.attack_detected:
            print(f"[INFO] Recovering Node {self.id}...")
            self.attack_detected = False
            self.traffic = 0
            self.cpu_usage = 0
            self.memory_load = 0

# 보완된 네트워크 클래스
class Network:
    def __init__(self, num_nodes, network_type='circular', bandwidth=10, latency=5, packet_loss_rate=0.1):
        self.num_nodes = num_nodes
        self.network_type = network_type
        self.bandwidth = bandwidth
        self.latency = latency
        self.packet_loss_rate = packet_loss_rate
        self.nodes = [Node(i, bandwidth, latency) for i in range(num_nodes)]
        self.edges = self.create_network()

    def create_network(self):
        edges = []
        if self.network_type == 'circular':
            for i in range(self.num_nodes):
                edges.append((i, (i + 1) % self.num_nodes))
        elif self.network_type == 'star':
            for i in range(1, self.num_nodes):
                edges.append((0, i))
        elif self.network_type == 'tree':
            for i in range(1, self.num_nodes):
                edges.append((i // 2, i))
        elif self.network_type == 'random':
            for i in range(self.num_nodes):
                for j in range(i + 1, self.num_nodes):
                    if random.random() > 0.5:
                        edges.append((i, j))
        return edges

# 보완된 가상 물리 시스템 클래스
class VirtualPhysicalSystem:
    def __init__(self, initial_temperature=20):
        self.temperature = initial_temperature
        self.hvac_state = False

    def update_temperature(self, traffic_load):
        if self.hvac_state:
            self.temperature -= 0.5  # 냉각
        self.temperature += 0.1 * traffic_load  # 트래픽 부하로 온도 상승

    def control_hvac(self, threshold):
        self.hvac_state = self.temperature > threshold

# CPS 피드백 루프 클래스
class CPSWithFeedback:
    def __init__(self, network, physical_system):
        self.network = network
        self.physical_system = physical_system

    def simulate_step(self, traffic):
        for i, node in enumerate(self.network.nodes):
            node.send_traffic(traffic[i])

        for edge in self.network.edges:
            src, dest = edge
            src_node = self.network.nodes[src]
            dest_node = self.network.nodes[dest]
            transfer_amount = min(src_node.traffic, dest_node.capacity)
            loss = random.random() < self.network.packet_loss_rate
            if not loss:
                src_node.receive_traffic(transfer_amount)
                dest_node.send_traffic(transfer_amount)

        # 공격 탐지
        for node in self.network.nodes:
            node.detect_attack()

        traffic_load = sum(node.traffic for node in self.network.nodes)
        self.physical_system.update_temperature(traffic_load)
        self.physical_system.control_hvac(30)

# 보완된 보안 시뮬레이션
class SecureCPS(CPSWithFeedback):
    def simulate_dos_attack(self, target_node_ids, attack_duration=5, recovery_steps=5):
        print(f"\n[ALERT] Simulating DoS attack on Nodes {target_node_ids}")
        attack_traffic = {node_id: [] for node_id in target_node_ids}

        for _ in range(attack_duration):
            for node_id in target_node_ids:
                attack_amount = random.randint(50, 150)  # 공격 강도를 증가
                self.network.nodes[node_id].send_traffic(attack_amount)
                attack_traffic[node_id].append(self.network.nodes[node_id].traffic)
                print(f"  - Node {node_id} traffic increased to {self.network.nodes[node_id].traffic}")

        print("\n[INFO] Attack Complete. Monitoring System Recovery...")

        # 공격 탐지 및 차단
        for node in self.network.nodes:
            if node.attack_detected:
                # 공격이 감지된 경우, 정상적인 트래픽을 다른 노드로 리디렉션
                print(f"[INFO] Redirecting traffic away from Node {node.id} due to attack.")
                for other_node in self.network.nodes:
                    if not other_node.attack_detected:
                        transfer_amount = min(node.traffic, other_node.capacity - other_node.traffic)
                        node.receive_traffic(transfer_amount)
                        other_node.send_traffic(transfer_amount)

        # 복구 시뮬레이션
        recovery_data = []
        for recovery_step in range(recovery_steps):
            for node in self.network.nodes:
                node.recover()  # 노드 복구
                if not node.attack_detected:  # 공격이 탐지되지 않은 노드만 트래픽 수신
                    node.receive_traffic(random.randint(10, 50))  # 시스템 트래픽 감소

            # 자원 모니터링 및 트래픽 조절
            for node in self.network.nodes:
                if node.is_overloaded():
                    print(f"  - Node {node.id} is overloaded. Redistributing traffic...")
                    for other_node in self.network.nodes:
                        if not other_node.is_overloaded() and other_node.id != node.id:
                            transfer_amount = min(node.traffic, other_node.capacity - other_node.traffic)
                            node.receive_traffic(transfer_amount)
                            other_node.send_traffic(transfer_amount)

            # 추가적인 트래픽 감소
            for node in self.network.nodes:
                if node.traffic > 0:
                    reduction_amount = min(node.traffic, 50)  # 최대 50만큼 트래픽 감소
                    node.receive_traffic(reduction_amount)

            recovery_status = {
                node_id: {
                    "traffic": self.network.nodes[node_id].traffic,
                    "cpu_usage": self.network.nodes[node_id].cpu_usage,
                    "memory_load": self.network.nodes[node_id].memory_load
                }
                for node_id in target_node_ids
            }
            recovery_data.append(recovery_status)
            print(f"  Recovery Step {recovery_step + 1}: {recovery_status}")

        print("[INFO] System recovered successfully.")
        return attack_traffic, recovery_data

# 평가 메트릭 추가
class EvaluationMetrics:
    @staticmethod
    def calculate_service_availability(traffic, total_capacity):
        return max(0, 100 * (1 - sum(traffic) / total_capacity))

    @staticmethod
    def calculate_average_recovery_time(recovery_data):
        total_time = 0
        for step_data in recovery_data:
            for node_data in step_data.values():
                if node_data["traffic"] > 0:
                    total_time += 1
        return total_time / len(recovery_data) if recovery_data else 0

# 트래픽 생성 함수
def generate_traffic(distribution_type='poisson', mean=5, stddev=2, size=10):
    if distribution_type == 'poisson':
        return np.random.poisson(mean, size)
    elif distribution_type == 'gaussian':
        return np.random.normal(mean, stddev, size)
    elif distribution_type == 'uniform':
        return np.random.uniform(0, mean, size)

# 시뮬레이션 실행 및 결과 분석
if __name__ == "__main__":
    network = Network(num_nodes=10, network_type='star')
    physical_system = VirtualPhysicalSystem()
    cps = SecureCPS(network, physical_system)

    temperatures = []
    traffic_loads = []

    print("[INFO] Starting CPS simulation...")
    for step in range(10):
        traffic = generate_traffic()
        cps.simulate_step(traffic)
        temperatures.append(physical_system.temperature)
        total_traffic = sum(node.traffic for node in cps.network.nodes)
        traffic_loads.append(total_traffic)
        print(f"Step {step + 1}: Total Traffic Load = {total_traffic}, Temperature = {physical_system.temperature:.2f}°C, HVAC State = {'ON' if physical_system.hvac_state else 'OFF'}")

    # 다수 노드 DoS 공격 시뮬레이션
    attack_nodes = [3, 5, 7]
    attack_traffic, recovery_data = cps.simulate_dos_attack(target_node_ids=attack_nodes)

    # 그래프 출력
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(range(1, 11), temperatures, marker='o')
    plt.title('Temperature Changes During Simulation')
    plt.xlabel('Step')
    plt.ylabel('Temperature (°C)')

    plt.subplot(3, 1, 2)
    plt.plot(range(1, 11), traffic_loads, marker='o', color='orange')
    plt.title('Traffic Load Changes During Simulation')
    plt.xlabel('Step')
    plt.ylabel('Total Traffic Load')

    plt.subplot(3, 1, 3)
    for node_id, traffic_data in attack_traffic.items():
        plt.plot(range(1, 6), traffic_data, marker='o', label=f'Node {node_id}')
    plt.title('DoS Attack Traffic on Target Nodes')
    plt.xlabel('Recovery Step')
    plt.ylabel('Traffic Load')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # 성능 메트릭 계산
    total_capacity = sum(node.capacity for node in network.nodes)
    service_availability = EvaluationMetrics.calculate_service_availability(traffic_loads, total_capacity)
    avg_recovery_time = EvaluationMetrics.calculate_average_recovery_time(recovery_data)

    print(f"\n[INFO] Service Availability: {service_availability:.2f}%")
    print(f"[INFO] Average Recovery Time: {avg_recovery_time:.2f} steps")
