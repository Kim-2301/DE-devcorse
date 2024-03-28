def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


def maxHeapify(self, i):
        left = 2*i
        right = 2*i+1

        smallest = i
        if left < len(self.data)and self.data[left] > self.data[smallest]:
            smallest = left

        if right < len(self.data)and self.data[right] > self.data[smallest]:
            smallest = right

        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.maxHeapify(smallest)
            
def insert(self, item):
        self.data.append(item)
        if len(self.data) < 2:
            return True
        else:
            idx = len(self.data) - 1
            while idx > 1 and self.data[idx] > self.data[idx // 2]:
                self.data[idx], self.data[idx // 2] = self.data[idx // 2], self.data[idx]
                idx //= 2
        return True