import { TProfile, TMovie } from "@/types/shared"

export const profileData: TProfile[] = [

	{
		key: 1,
		name: "John Wick",
		bio: "I love my wife.",
		avatarUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQg1-p5Lm1aLS15QoavG09CjnyICW1TWLvag&s",
		isOnline: false,

	},
	{
		key: 2,
		name: "Gukeyo Van Rossum",
		bio: "I'do love playing with Pythons.",
		avatarUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0_pwz_hkGNK9C2jLQ_XQqrf0W36h4KbRB6A&s",
		isOnline: true,
	},
	{
		key: 3,
		name: "Dennis Ritchie",
		bio: "If you're bad, I'm your dad.",
		avatarUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUphubhu3iY4sBlVzOa9L1UhTWci9PBcyd-w&s",
		isOnline: true,
	},
	{
		key: 4,
		name: "Don Lee",
		bio: "(Look at you :)",
		avatarUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTtCPQVsiksC8ZFEOS3wuInHi4diKWGMn54w&s",
		isOnline: false,
	}
]


export const books: TMovie[] = [
	{
		key: 1,
		name: "Ratchasan",
		director: "Tamilan",
		genre: "triller",
	},
	{
		key: 2,
		name: "Anjaam Pathira",
		director: "no-body",
		genre: "triller",
	},
	{
		key: 3,
		name: "Sitaramam",
		director: "Telungu",
		genre: "love",
	},
	{
		key: 4,
		name: "Premam",
		director: "Malayalam",
		genre: "love",
	},
]
