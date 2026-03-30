import streamlit as st
st.title('My first project!!!')
txt_data = '''
# 📘 이차방정식(Quadratic Equation)

## 1. 이차방정식이란?
이차방정식은 다음과 같은 형태의 방정식을 말합니다.

\[
ax^2 + bx + c = 0
\]

- \(a, b, c\)는 상수이며, \(a \neq 0\)
- 미지수 \(x\)의 최고 차수가 2인 방정식

---

## 2. 이차방정식의 해(근)
이차방정식의 해는 다음과 같은 **근의 공식**을 이용하여 구할 수 있습니다.

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

- \(b^2 - 4ac\)를 **판별식**(Discriminant)이라고 합니다.

---

## 3. 판별식에 따른 해의 개수

| 판별식 \(D = b^2 - 4ac\) | 해의 개수 | 설명 |
|--------------------------|-----------|------|
| \(D > 0\) | 서로 다른 두 실근 | 서로 다른 두 해를 가짐 |
| \(D = 0\) | 중근 | 같은 해를 두 번 가짐 |
| \(D < 0\) | 허근 (복소수 해) | 실수가 아닌 해 |

---

## 4. 풀이 방법

### (1) 인수분해
\[
x^2 - 5x + 6 = 0
\]
\[
(x - 2)(x - 3) = 0
\]
\[
x = 2, 3
\]

---

### (2) 완전제곱식
\[
x^2 + 4x + 1 = 0
\]
\[
(x + 2)^2 - 3 = 0
\]

---

### (3) 근의 공식 사용
모든 이차방정식에 적용 가능

---

## 5. 그래프와의 관계
이차방정식 \(ax^2 + bx + c = 0\)은 포물선의 방정식과 관련이 있습니다.

- 그래프: \(y = ax^2 + bx + c\)
- 해의 개수 = x축과 만나는 점의 개수

---

## 6. 핵심 정리 ✨

- 이차방정식은 최고차항이 \(x^2\)인 방정식이다.
- 근의 공식을 통해 항상 해를 구할 수 있다.
- 판별식을 통해 해의 개수와 종류를 알 수 있다.
- 그래프(포물선)와 밀접한 관계가 있다.

---
'''
c1, c2 = st.columns((4, 1))
with c1:
    with st.expander('Contents...'):
        url='https://www.youtube.com/watch?v=ys7BVi9cpig'
        st.video(url)
        st.subheader('This is left!!!')
        st.markdown(txt_data)

with c2:
    with st.expander('Tips...'):
        imglink='https://mblogthumb-phinf.pstatic.net/MjAyNTExMjlfMzYg/MDAxNzY0MzgxNjQxNjk4.Ufj989hww6ZplUY5gH1trYhAvseBYU9UjKb7HjGE794g.9cIwrHLBq_5HLtXwJTrlo1Wq_q93LGKOsmZU8C_n37gg.GIF/%EC%98%AC%EB%9D%BC%ED%94%84_%EB%A1%9C%EB%B4%87_04_%EC%BD%94.gif?type=w800'
        st.image(imglink)
        st.info('This is right!!!')

c3, c4 = st.columns((4, 1))
with c3:
    with st.expander('Contents...'):
        url='https://www.youtube.com/watch?v=ys7BVi9cpig'
        st.video(url)
        st.subheader('This is left!!!')
        st.markdown(txt_data)

with c4:
    with st.expander('Tips...'):
        imglink='https://mblogthumb-phinf.pstatic.net/MjAyNTExMjlfMzYg/MDAxNzY0MzgxNjQxNjk4.Ufj989hww6ZplUY5gH1trYhAvseBYU9UjKb7HjGE794g.9cIwrHLBq_5HLtXwJTrlo1Wq_q93LGKOsmZU8C_n37gg.GIF/%EC%98%AC%EB%9D%BC%ED%94%84_%EB%A1%9C%EB%B4%87_04_%EC%BD%94.gif?type=w800'
        st.image(imglink)
        st.info('This is right!!!')
