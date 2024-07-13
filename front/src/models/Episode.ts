export class EpisodeDTO {
    id = 0;
    saison = 0;
    episode = 0;
    nom: null | string = null;
  }
  
  export class Episode extends EpisodeDTO {
    constructor(data?: Episode | EpisodeDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }