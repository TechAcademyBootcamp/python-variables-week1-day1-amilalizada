# Əvvəlcə math modulunu import edirik.
# Əks halda onun imkanlarından yararlana bilməyəcəyik
import math

# math.ceil(x) - kəsr ədədini yuxarıya doğru yuvarlaqlaşdırma
# ====================================================


# math.ceil(x) funksiyasını özünüz yazmağa çalışın
x=10.7
print(f"{x} ədədinin yuxarı yuvarlaqlaşdırılmış dəyəri:", math.ceil(x))
# =====================================================

# math.floor(x) - kəsr ədədini aşağıya doğru yuvarlaqlaşdırır
# ====================================================
x = 12.1
print(f"{x} ədədinin yuxarı yuvarlaqlaşdırılmış dəyəri:", math.floor(x))


# ====================================================

# math.fabs(x) - ədədin müsbət dəyərini qaytarır
# ====================================================

x = -12.1
print(f"{x} ədədinin müsbət dəyəri:", math.fabs(x))

# math.fabs(x) funksiyasını özünüz yazmağa çalışın
x=-2
print(f"{x} ədədinin müsbət dəyəri:", math.fabs(x))

# ====================================================

# math.isclose(a, b, rel_tol) - ədədlərin yaxınlığını hesablayır
# ====================================================

# ====================================================

# math.isclose(a, b, rel_tol) funksiyasını özünüz yazmağa çalışın
a = 1
b = 2
rel_tol = 0.5
print(f"{a} və {b} ədədləri", "yaxındır" if math.isclose(a, b, rel_tol=rel_tol) else "yaxın deyil")