export class NavigationConst {
    public static readonly nomApp = 'Série Tracker';
  
    // login
    public static readonly routeLogin = '/';
    public static readonly nameLogin = 'Login';
    public static readonly titleLogin = 'Connexion';

    // SignUp
    public static readonly routeSignUp = '/signup'
    public static readonly nameSignUp = 'SignUp'
    public static readonly titleSignup = "Enregistrement"

    // Home
    public static readonly routeHome = '/home'
    public static readonly nameHome = 'Home'
    public static readonly titleHome = 'Home'

    public static readonly routeSerie = '/serie/:id'
    public static readonly nameSerie = 'Serie'
    public static readonly titleSerie = 'Séries'

    public static readonly routeArchive = '/archive'
    public static readonly nameArchive = 'Archive'
    public static readonly titleArchive = 'Séries archivées'

    // Followed Series
    public static readonly routeFollowed = '/followed'
    public static readonly nameFollowed = 'Followed'
    public static readonly titleFollowed = 'Séries suivies'

    public static readonly routeFollowedDetail = '/followed/:id'
    public static readonly nameFollowedDetail = 'FollowedDetail'
    public static readonly titleFollowedDetail = 'Détail de la série suivie'

    // Partage
    public static readonly routeShare = '/share'
    public static readonly nameShare = 'Share'
    public static readonly titleShare = 'Partage'
  }
  