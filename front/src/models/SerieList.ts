export class SerieListDTO {
    id = 0;
    nom = ''
    est_archive = false
  }
  
  export class SerieList extends SerieListDTO {
    constructor(data?: SerieList | SerieListDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }