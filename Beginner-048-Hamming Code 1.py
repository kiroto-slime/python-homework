n=int(input())
ppos=[1,2,4,8,16]
for i in range(n):
    s=input().strip()
    x=int(s,16)
    b=bin(x)[2:].zfill(16)
    arr=[0]*22
    idx=0
    for e in range(1,22):
        if e not in ppos:
            arr[e]=int(b[idx])
            idx+=1
    for p in ppos:
        sm=0
        for e in range(1,22):
            if e&p:
                sm^=arr[e]
        arr[p]=sm
    print(''.join(str(arr[p]) for p in ppos))
 
  
  #說明
  # 讀取第一行，表示後續有 n 筆 16 位元資料
  n = int(input())
  # 預先定義檢查位所在位置（1, 2, 4, 8, 16）
  ppos = [1, 2, 4, 8, 16]
  # 使用 for 迴圈處理 n 筆輸入
  for _ in range(n):
      # 讀取 16 進制字串並去除前後空白
      s = input().strip()
      # 將 16 進制字串轉為整數
      x = int(s, 16)
      # 將整數轉為二進制，去除 '0b' 並補齊至 16 位
      b = bin(x)[2:].zfill(16)
      # 建立一個長度 22 的陣列（index 0 不使用），預留 21 位
      arr = [0] * 22
      # 用來追蹤資料位放入 b 的哪個 index
      idx = 0
      # 迴圈 1~21 將 16 位資料填入非檢查位
      for i in range(1, 22):
          # 若 i 不是檢查位，則放入資料
          if i not in ppos:
              arr[i] = int(b[idx])
              idx += 1
      # 計算 5 個檢查位的值
      for p in ppos:
          # sm 用來累加 XOR 結果
          sm = 0
          # 逐位檢查在該位元 p 下，哪些位置需要被校驗
          for i in range(1, 22):
              # 如果 i 的二進制與 p 的位元重疊 (i & p != 0)
              if i & p:
                  # 將該位置的位元與 sm 做 XOR
                  sm ^= arr[i]
          # 最後將檢查位設定為 sm 的值
          arr[p] = sm
      # 最後將 5 個檢查位 P1, P2, P3, P4, P5 的值串接印出
      print(''.join(str(arr[p]) for p in ppos))
