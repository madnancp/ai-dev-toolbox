export interface TProfile {
	key: number,
	name: string,
	bio?: string,
	avatarUrl?: string,
	isOnline: boolean,
}

export interface TMovie {
	key: number,
	name: string
	director: string
	genre: string
}
