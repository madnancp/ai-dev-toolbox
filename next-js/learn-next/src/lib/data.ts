import { TProfile, TMovie } from "@/types/shared"

export const profileData: TProfile[] = [

	{
		name: "John Wick",
		bio: "I love my wife.",
		avatarUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQg1-p5Lm1aLS15QoavG09CjnyICW1TWLvag&s",
		online: true,

	},
	{
		name: "Guido Van Rossum",
		bio: "I'do love playing with Pythons.",
		avatarUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0_pwz_hkGNK9C2jLQ_XQqrf0W36h4KbRB6A&s",
		online: true,
	},
	{
		name: "Dennis Ritchie",
		bio: "If you're bad, I'm your dad.",
		avatarUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUphubhu3iY4sBlVzOa9L1UhTWci9PBcyd-w&s",
		online: true,
	},
	{
		name: "Don Lee",
		bio: "(Look at you :)",
		avatarUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTtCPQVsiksC8ZFEOS3wuInHi4diKWGMn54w&s",
		online: false,
	}
]


export const books: TMovie[] = [
	{
		name: "Ratchasan",
		director: "Tamilan",
		genre: "triller",
	},
	{
		name: "Anjaam Pathira",
		director: "no-body",
		genre: "triller",
	},
	{
		name: "Sitaramam",
		director: "Telungu",
		genre: "love",
	},
	{
		name: "Premam",
		director: "Malayalam",
		genre: "love",
	},
]
