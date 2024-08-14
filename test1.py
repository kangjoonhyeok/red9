import cv2

# 카메라 캡쳐 객체 생성 (0은 기본 카메라를 의미)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# 이미지 캡쳐
ret, frame = cap.read()

if not ret:
    print("이미지를 캡쳐할 수 없습니다.")
    exit()

# 이미지 표시
cv2.imshow('Captured Image', frame)

# 키 입력 대기 (0은 무한 대기)
cv2.waitKey(0)

# 창 닫기
cv2.destroyAllWindows()

# 카메라 해제
cap.release()
