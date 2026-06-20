from roboflow import Roboflow
from ultralytics import YOLO

# --- PHẦN 1: TẢI DỮ LIỆU TỪ ROBOFLOW ---
rf = Roboflow(api_key="yvAguzDbAPqn2wvUVC7j")
project = rf.workspace("thng-phm-s-workspace").project("alpr_hcmute")
version = project.version(1)
dataset = version.download("yolov8")

# --- PHẦN 2: HUẤN LUYỆN MÔ HÌNH ---
# Bắt buộc phải có khối if __name__ == '__main__' khi chạy local trên Windows
if __name__ == '__main__':
    print("Khởi tạo mô hình YOLOv8n...")
    model = YOLO('yolov8n.pt')  # Tự động tải file trọng số ban đầu

    print("Bắt đầu huấn luyện...")
    results = model.train(
        data=f"{dataset.location}/data.yaml", # Trỏ tới file data vừa tải về
        epochs=50,                            # Số vòng lặp
        imgsz=640,                            # Kích thước ảnh
        plots=True                            # Xuất biểu đồ để báo cáo
    )
    print("Huấn luyện hoàn tất! File kết quả nằm trong thư mục 'runs/detect/train'")