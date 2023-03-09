# Python program for stable marriage problem
# Jumlah Pria atau wanita
N = 4

# Fungsi ini mengembalikan true jika
# wanita 'w' lebih suka pria 'm1' daripada pria 'm'
def wPrefersM1OverM(prefer, w, m, m1):
	
	# Periksa apakah w lebih suka m daripada dia
    # keterlibatan saat ini m1
	for i in range(N):
		
		# Jika m1 datang sebelum m dalam daftar w,
        # lalu w lebih suka pertunangannya saat ini,
        # jangan lakukan apapun
		if (prefer[w][i] == m1):
			return True

		# Jika m muncul sebelum m1 dalam daftar w,
        # lalu bebaskan pertunangannya saat ini
        # dan libatkan dia dengan m
		if (prefer[w][i] == m):
			return False

# Mencetak pencocokan stabil untuk N anak laki-laki dan N anak perempuan.
# Anak laki-laki diberi nomor 0 sampai N-1.
# Anak perempuan diberi nomor N sampai 2N-1.
def stableMarriage(prefer):
	
# Toko mitra wanita. Ini adalah keluaran kami
# array yang menyimpan informasi yang lewat.
# Nilai wPartner[i] menunjukkan partner
# ditugaskan untuk wanita N+i. Perhatikan bahwa nomor wanita
# antara N dan 2*N-1. Nilai -1 menunjukkan
# wanita ke-(N+i) itu bebas
	wPartner = [-1 for i in range(N)]

# Array untuk menyimpan ketersediaan pria.
# Jika mFree[i] salah, maka man 'i' bebas,
# sebaliknya bertunangan.
	mFree = [False for i in range(N)]

	freeCount = N

# Mumpung ada orang bebas
	while (freeCount > 0):
		
		# Pilih orang bebas pertama (kami dapat memilih siapa saja)
		m = 0
		while (m < N):
			if (mFree[m] == False):
				break
			m += 1

		# Satu per satu pergi ke semua wanita menurut preferensi 
        # # m. Di sini m adalah orang bebas yang dipilih
		i = 0
		while i < N and mFree[m] == False:
			w = prefer[m][i]

		# Wanita pilihan bebas,
        # w dan m menjadi mitra (Perhatikan bahwa
        # kemitraan mungkin berubah nanti).
        # Jadi bisa dibilang mereka bertunangan bukan menikah
			if (wPartner[w - N] == -1):
				wPartner[w - N] = m
				mFree[m] = True
				freeCount -= 1

			else:
				
				# Jika w tidak gratis
                # Temukan keterlibatan w saat ini
				m1 = wPartner[w - N]

				# Jika w lebih memilih m daripada pertunangannya saat ini m1,
                # lalu putuskan ikatan antara w dan m1 dan
                # libatkan m dengan w.
				if (wPrefersM1OverM(prefer, w, m, m1) == False):
					wPartner[w - N] = m
					mFree[m] = True
					mFree[m1] = False
			i += 1

			# Akhir dari Lain
# Akhir dari for loop yang berjalan
# untuk semua wanita dalam daftar m
# Akhir dari main while loop

	# Print solusi 
	print("Woman ", " Man")
	for i in range(N):
		print(i + N, "\t", wPartner[i])

# Driver Code
prefer = [[7, 5, 6, 4], [5, 4, 6, 7],
		[4, 5, 6, 7], [4, 5, 6, 7],
		[0, 1, 2, 3], [0, 1, 2, 3],
		[0, 1, 2, 3], [0, 1, 2, 3]]

stableMarriage(prefer)