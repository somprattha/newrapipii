import os

# ตั้งค่าโฟลเดอร์ที่เก็บโมเดล
model_folder = r"F:\Steam\steamapps\common\VTube Studio\VTube Studio_Data\StreamingAssets\Live2DModels"

def list_expressions(model_folder):
    # ค้นหาทุกไฟล์ .exp3.json
    expressions = []
    for root, dirs, files in os.walk(model_folder):
        for file in files:
            if file.endswith(".exp3.json"):
                expressions.append(os.path.join(root, file))
    
    return expressions

expressions = list_expressions(model_folder)

if expressions:
    print("พบ Expression เหล่านี้:")
    for expression in expressions:
        print(expression)
else:
    print("ไม่พบ Expression ใดๆ")
