# main.py
import asyncio
from pyscript import document
from algorithm import bubble_sort_generator  # 完美引入外部模組

# 視圖 (View)：只負責畫圖
def render_bars(arr, active_indices):
    container = document.querySelector("#visualizer")
    container.innerHTML = ""
    for i, val in enumerate(arr):
        div = document.createElement("div")
        div.className = "bar"
        div.style.height = f"{val}px"
        div.innerText = str(val)
        if i in active_indices:
            div.style.backgroundColor = "#e74c3c"
        container.appendChild(div)

# 控制器 (Controller)：黏合 Model 與 View
async def start_animation(event):
    data = [80, 40, 120, 60, 160, 20, 100]
    
    # 建立生成器
    sorter = bubble_sort_generator(data)
    
    # 迴圈讀取演算法的每一步狀態，並控制動畫時間
    for current_arr, idx1, idx2 in sorter:
        render_bars(current_arr, [idx1, idx2])
        await asyncio.sleep(0.5) # 控制器負責處理 UI 暫停，演算法層完全不管

    # 排序完成的最終渲染
    render_bars(data, [])

document.querySelector("#sort-btn").addEventListener("click", start_animation)
