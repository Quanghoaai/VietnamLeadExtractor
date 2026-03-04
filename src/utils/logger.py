import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """
    Khởi tạo và cấu hình logger tiêu chuẩn cho hệ thống.
    Thay vì sử dụng print, dự án yêu cầu luôn sử dụng logger này để format log,
    dễ dàng trace lại và theo dõi trên các hệ thống giám sát.
    
    Args:
        name (str): Tên logger (thường truyền bằng tham số __name__).
        
    Returns:
        logging.Logger: Đối tượng logger đã được cấu hình định dạng xuất chuẩn PEP8.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        # Sử dụng format rõ ràng bao gồm thời gian, tên module, level và chi tiết thông báo
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
    return logger
