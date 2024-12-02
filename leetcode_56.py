class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

    # Aralıkları başa göre sıralama
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]  # İlk aralığı ekle [1, 3]

#Her bir aralık, son birleştirilen aralıkla karşılaştırılır. Eğer çakışma varsa, birleştirilir. 
#Aksi halde, yeni aralık olarak eklenir.
        for current in intervals[1:]:
            last_merged = merged[-1] # [1, 3]
        # Eğer mevcut aralık, son birleştirilen aralıkla çakışıyorsa
            if current[0] <= last_merged[1]:#current[0] = 2, last_merged[1] = 3
            # Aralıkları birleştir
                last_merged[1] = max(last_merged[1], current[1])
            else:
            # Çakışmıyorsa, mevcut aralığı ekle
                merged.append(current)

        return merged
