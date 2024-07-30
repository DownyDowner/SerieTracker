import { SerieList } from "./SerieList";

export class SuiviDTO {
    id = 0;
    serie: SerieList = new SerieList();
    
  }
  
  export class Suivi extends SuiviDTO {
    constructor(data?: Suivi | SuiviDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }