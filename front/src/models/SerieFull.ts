import { Episode } from "./Episode";

export class SerieFullDTO {
    id = 0;
    nom = ''
    est_archive = false
    episodes: Episode[] = [];
  }
  
  export class SerieFull extends SerieFullDTO {
    constructor(data?: SerieFull | SerieFullDTO | null) {
      super();
      if (data) {
        Object.assign(this, data);
        this.episodes = data.episodes.map((e) => new Episode(e));
      }
    }
  }
  