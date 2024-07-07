import pyaudio

class AudioPlayer():
    def __init__(self):
        self.chunk = 1024
        self.audio = pyaudio.PyAudio()
        self._running = True


    def play(self, audiopath):
        self._running = True
        #storing how much we have read already
        self.chunktotal = 0
        wf = wave.open(audiopath, 'rb')
        stream = self.audio.open(format =self.audio.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(),rate = wf.getframerate(),output = True)
        print(wf.getframerate())
        # read data (based on the chunk size)
        data = wf.readframes(self.chunk)
        #THIS IS THE TOTAL LENGTH OF THE AUDIO
        audiolength = wf.getnframes() / float(wf.getframerate())

        while self._running:
            if data != '':
                stream.write(data)
                self.chunktotal = self.chunktotal + self.chunk
                #calculating the percentage
                percentage = (self.chunktotal/wf.getnframes())*100
                #calculating the current seconds
                current_seconds = self.chunktotal/float(wf.getframerate())
                data = wf.readframes(self.chunk)

            if data == b'':
                break

        # cleanup stream
        stream.close()

    def stop(self):
        self._running = False