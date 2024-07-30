export class SuiviDTO {
    id = 0;
    serie = 0
  }
  
  export class Suivi extends SuiviDTO {
    constructor(data?: Suivi | SuiviDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }