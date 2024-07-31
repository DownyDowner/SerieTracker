export class EpisodeStatusDTO {
    id = 0;
    saison = 0;
    episode = 0;
    nom: string | null = null;
    seen = false;
    seen_date: string | null = null;
  }
  
  export class EpisodeStatus extends EpisodeStatusDTO {
    constructor(data?: EpisodeStatus | EpisodeStatusDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }