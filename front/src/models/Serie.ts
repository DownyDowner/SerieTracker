export class SerieDTO {
    id = 0;
    nom = ''
    est_archive = false
  }
  
  export class Serie extends SerieDTO {
    constructor(data?: Serie | SerieDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }