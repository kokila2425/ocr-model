from paddleocr import PaddleOCR
import cv2

ocr = PaddleOCR(
    lang='japan',
    use_angle_cls=True,
    det=True,
    rec=True
)

img = cv2.imread("img.png")
img = cv2.resize(img, None, fx=2, fy=2)

result = ocr.ocr(img, cls=True)

for line in result[0]:
    print(line[1][0])
