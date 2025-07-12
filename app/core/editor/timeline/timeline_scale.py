from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt

class TimelineScale:
    """
    Zaman çizelgesinin ölçeklendirme mantığını yönetir.
    QSlider ile piksel/saniye oranını ayarlar.
    """
    def __init__(self, slider: QSlider):
        self.slider = slider
        self.min_pixel_per_second = 10.0  # Minimum uzaklaştırma (örn. 1 saniye = 10 piksel)
        self.max_pixel_per_second = 200.0 # Maksimum yakınlaştırma (örn. 1 saniye = 200 piksel)
        
        # Slider'ın min/max değerlerini ayarla (bu aralığı piksel/saniye aralığına eşleyeceğiz)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100) # Örneğin, 0-100 arasında bir slider değeri
        self.slider.setValue(25) # Başlangıç değeri (örn. varsayılan bir yakınlaştırma)

        self.current_pixel_per_second = self._map_slider_value_to_scale(self.slider.value())
        
        # Slider'ın değeri değiştiğinde ölçeği güncelle
        self.slider.valueChanged.connect(self._on_slider_value_changed)

    def _map_slider_value_to_scale(self, slider_value: int) -> float:
        """Slider değerini piksel/saniye oranına eşler."""
        # Basit doğrusal eşleme: (slider_value / max_slider_value) * (max_pps - min_pps) + min_pps
        # Daha yumuşak geçişler için logaritmik eşleme de kullanılabilir.
        normalized_value = slider_value / self.slider.maximum()
        return self.min_pixel_per_second + normalized_value * (self.max_pixel_per_second - self.min_pixel_per_second)

    def _on_slider_value_changed(self, value: int):
        """Slider değeri değiştiğinde tetiklenir."""
        self.current_pixel_per_second = self._map_slider_value_to_scale(value)
        print(f"Ölçek güncellendi: {self.current_pixel_per_second:.2f} piksel/saniye")
        # Cetvelin ve kliplerin yeniden çizilmesi için bir sinyal yayılabilir
        # Örneğin: self.scale_changed.emit(self.current_pixel_per_second)
        
        # Şimdilik doğrudan TimelineRuler'ı güncelleyeceğiz (ileride sinyal/slot ile daha iyi olur)
        if hasattr(self, 'ruler_ref'): # TimelineRuler referansı varsa
            self.ruler_ref.set_scale_factor(self.current_pixel_per_second)
        
        # Kliplerin de geometry'lerini güncellemesi gerekecek
        # Bu kısım TimelineEditorDockWidget içinde yönetilebilir

    def get_current_pixel_per_second(self) -> float:
        """Mevcut piksel/saniye oranını döndürür."""
        return self.current_pixel_per_second

    def set_pixel_per_second(self, pps: float):
        """Piksel/saniye oranını programatik olarak ayarlar ve slider'ı günceller."""
        # Ters eşleme yaparak slider değerini bul
        normalized_value = (pps - self.min_pixel_per_second) / (self.max_pixel_per_second - self.min_pixel_per_second)
        slider_value = int(normalized_value * self.slider.maximum())
        self.slider.setValue(slider_value) # Bu aynı zamanda _on_slider_value_changed'ı tetikleyecektir