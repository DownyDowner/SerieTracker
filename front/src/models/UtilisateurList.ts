export class UtilisateurListDTO {
    id = 0;
    username = "";
    partage_avec = false;
  }
  
  export class UtilisateurList extends UtilisateurListDTO {
    constructor(data?: UtilisateurList | UtilisateurListDTO | null) {
      super();
      if (data) Object.assign(this, data);
    }
  }