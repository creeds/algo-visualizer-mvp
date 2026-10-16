import asyncio
from pyscript import document
from algorithm import bubble_sort_generator

# 準備一個簡單的 log 函數，把文字塞進 HTML 裡
def write_log(msg):
    log_div = document.querySelector("#log")
    # 將新訊息加到最上方，方便手機觀看
    log_div.innerHTML = f"<div>{msg}</div>" + log_div.innerHTML

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

async def start_animation(event):
    btn = document.querySelector("#sort-btn")
    btn.disabled = True
    write_log("▶ 開始執行排序...")
    
    data = [80, 40, 120, 60, 160, 20, 100]
    sorter = bubble_sort_generator(data)
    
    try:
        step_count = 1
        for current_arr, idx1, idx2 in sorter:
            write_log(f"第 {step_count} 步: 比較 index {idx1} 與 {idx2}")
            render_bars(current_arr, [idx1, idx2])
            await asyncio.sleep(0.5) 
            step_count += 1
            
        render_bars(data, [])
        write_log("✅ 排序完成！")
    except Exception as e:
        # 如果執行過程有錯誤，把它印在網頁上！
        write_log(f"❌ 發生錯誤: {str(e)}")
        
    btn.disabled = False

# 初次載入時先畫出預設的圖表
render_bars([80, 40, 120, 60, 160, 20, 100], [])

document.querySelector("#sort-btn").addEventListener("click", start_animation)
write_log("系統準備就緒。")
