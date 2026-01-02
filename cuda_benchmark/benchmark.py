import time
import numpy as np
import torch

def matrix_multiplication(size=2048):
    print(f"\nТестируем умножение матриц {size}x{size}")

    # CPU версия (NumPy)
    a_cpu = np.random.rand(size, size).astype(np.float32)
    b_cpu = np.random.rand(size, size).astype(np.float32)

    start = time.time()
    c_cpu = np.dot(a_cpu, b_cpu)
    cpu_time = time.time() - start
    print(f"CPU (NumPy): {cpu_time:.4f} сек")

    # CUDA версия (PyTorch)
    if torch.cuda.is_available():
        device = torch.device("cuda")
        a_gpu = torch.randn(size, size, device=device, dtype=torch.float32)
        b_gpu = torch.randn(size, size, device=device, dtype=torch.float32)

        # Прогрев GPU
        for _ in range(3):
            torch.matmul(a_gpu, b_gpu)

        torch.cuda.synchronize()
        start = time.time()
        c_gpu = torch.matmul(a_gpu, b_gpu)
        torch.cuda.synchronize()
        gpu_time = time.time() - start
        print(f"GPU (CUDA): {gpu_time:.4f} сек")
        print(f"Ускорение: {cpu_time / gpu_time:.2f}x")
    else:
        print("CUDA недоступна на этой машине")


if __name__ == "__main__":
    print("Сравнение производительности CPU vs CUDA\n")
    matrix_multiplication(size=2048)
    matrix_multiplication(size=4096)