import segno
import base64
from io import BytesIO

def generate_report_qr(report, stations):
    # Формируем информацию для QR-кода
    info = f"Отчет №{report.id} Дата:{report.report_date}\n\n"
    stations_count = 0
    for station in stations:
        stations_count +=1
        info += f"Станция №{station['station_id']} {station['short_name']} Потребление энергии: {station['power']} || \n"
    
    info += f"\n Количество станций: {stations_count} Суммарное энергопотребление = {report.sum_power}\n\n"
    # Генерация QR-кода
    qr = segno.make(info)
    buffer = BytesIO()
    qr.save(buffer, kind='png')
    buffer.seek(0)

    # Конвертация изображения в base64
    qr_image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    return qr_image_base64