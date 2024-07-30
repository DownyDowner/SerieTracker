export class SuiviCreationDTO {
    serie: number = 0; 
  }
  
  export class SuiviCreation extends SuiviCreationDTO {
    constructor(data?: SuiviCreation | SuiviCreationDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }