import pyaudio

class AudioPlayer():
    def __init__(self):
        self.chunk = 1024
        self.audio = pyaudio.PyAudio()
        self._running = True


    def play(self, audiopath):
        self._running = True
        self.chunktotal = 0
        wf = wave.open(audiopath, 'rb')
        stream = self.audio.open(format =self.audio.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(),rate = wf.getframerate(),output = True)
        print(wf.getframerate())
        data = wf.readframes(self.chunk)
        audiolength = wf.getnframes() / float(wf.getframerate())

        while self._running:
            if data != '':
                stream.write(data)
                self.chunktotal = self.chunktotal + self.chunk
                percentage = (self.chunktotal/wf.getnframes())*100
                current_seconds = self.chunktotal/float(wf.getframerate())
                data = wf.readframes(self.chunk)

            if data == b'':
                break

        stream.close()

    def stop(self):
        self._running = False