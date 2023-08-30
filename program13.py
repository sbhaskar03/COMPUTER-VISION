import cv2
import numpy as np

p = r"C:\Users\mainu\Videos\SnapTik.biz-Doctor - Chellamma Lyric _ Sivakarthikeyan _ Anirudh Ravichander _ Nelson Dilipkumar _ Jonita Gandhi-(1080p).mp4"
c = cv2.VideoCapture(p)

p1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
p2 = np.float32([[100, 50], [300, 0], [0, 300], [300, 300]])
m = cv2.getPerspectiveTransform(p1, p2)

while True:
    ret, r = c.read()
    if not ret:
        break

    r1 = cv2.resize(r, (700, 700))
    d = cv2.warpPerspective(r1, m, (700, 700))
    cv2.imshow("a", d)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

c.release()
cv2.destroyAllWindows()
