import cv2
import time
import serial
import base64

# 시리얼 포트 설정
serial_port = '/dev/ttyAMA1'
baud_rate = 115200

# 시리얼 통신 설정
ser = serial.Serial(serial_port, baud_rate, timeout=1)

def capture_image():
    # 카메라 초기화
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return None
    
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        print("이미지를 캡처할 수 없습니다.")
        return None
    
    # 이미지 크기 변경 (680x480)
    resized_frame = cv2.resize(frame, (680, 480))
    
    # JPEG 형식으로 이미지 인코딩
    ret, jpeg = cv2.imencode('.jpg', resized_frame)
    
    if not ret:
        print("이미지를 JPEG로 인코딩할 수 없습니다.")
        return None
    
    return jpeg.tobytes()

def send_image_data(image_data):
    # Base64 인코딩
    encoded_data = base64.b64encode(image_data)
    
    # 데이터 크기 전송
    data_size = len(encoded_data)
    
    # 청크 단위로 데이터 전송
    chunk_size = 1024  # 청크 크기
    for i in range(0, data_size, chunk_size):
        chunk = encoded_data[i:i+chunk_size]
        ser.write(chunk)
        print(chunk)
        
        time.sleep(0.20)  # 청크 간 잠시 대기
    ser.write(b'END\n')

try:
    
        image_data = capture_image()
        
        if image_data is not None:
            # 사진 데이터 전송
            send_image_data(image_data)
            print("전송 완료!")
            
        # 잠시 대기
        time.sleep(5)

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    # 자원 해제
    ser.close()
