export class VuDTO {
    id = 0;
    episode = 0;
    date = "";
  }
  
  export class Vu extends VuDTO {
    constructor(data?: Vu | VuDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }