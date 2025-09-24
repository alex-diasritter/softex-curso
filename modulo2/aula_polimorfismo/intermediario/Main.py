from modulo2.aula_polimorfismo.intermediario.Midia import Midia
from modulo2.aula_polimorfismo.intermediario.Musica import Musica
from modulo2.aula_polimorfismo.intermediario.Video import Video

class Main:

    musica = Musica("Peaceful Day", 3.15, "Pennywise")
    musica2 = Musica("American Jesus", 2.35, "Bad Religion")
    musica3 = Musica("I Was Wrong", 4.23, "Social Distortion")

    video = Video("Fight Club", 134.50, "1280x720")
    video2 = Video("Titanic", 112.70, "1280x720")
    video3 = Video("Tha Batman", 165.70, "1280x720")

    colection:dict[str, list[Midia]] = {"musicas": [], "videos": []}

    colection["musicas"].append(musica)
    colection["musicas"].append(musica2)
    colection["musicas"].append(musica3)

    colection["videos"].append(video)
    colection["videos"].append(video2)
    colection["videos"].append(video3)

    for lista in colection.values():
        for item in lista:
            item.exibir()