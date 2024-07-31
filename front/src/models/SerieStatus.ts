import { EpisodeStatus } from "./EpisodeStatus";

export class SerieStatusDTO {
    id = 0;
    nom = '';
    est_archive = false;
    episodes: EpisodeStatus[] = [];
  }
  
  export class SerieStatus extends SerieStatusDTO {
    constructor(data?: SerieStatus | SerieStatusDTO | null) {
      super();
      if (data) {
        Object.assign(this, data);
        this.episodes = data.episodes.map((e) => new EpisodeStatus(e));
      }
    }
  }