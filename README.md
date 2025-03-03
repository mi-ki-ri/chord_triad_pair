# Triad Pair

## About

このコードは、音楽理論に基づいてトライアド（3 和音）を他のコード（和音）と組み合わせるための Python スクリプトです。pychord ライブラリを使用してコードの構成要素を取得し、colorama ライブラリを使用してターミナル出力を色付けしています。

merge_triads 関数は、与えられたトライアドを他のすべてのベース音とアペンディックス（コードの種類）と組み合わせて、新しいコードを生成します。生成されたコードの構成要素を取得し、トライアドの構成要素と組み合わせて一意の音のリストを作成します。このリストをソートし、各音がトライアドの構成要素に含まれているか、C メジャースケールに含まれているか、それ以外かに応じて色分けして表示します。

Chord クラスは、コードの名前、ルート音、クオリティ（コードの種類）、追加された音、スラッシュコードのベース音などの属性を持ちます。components メソッドは、コードの構成要素を返します。init 関数は、colorama ライブラリの初期化を行い、ターミナル出力を色付けするための設定を行います。

スクリプトの最後では、いくつかのトライアド（例：C、Am、G）を定義し、merge_triads 関数を呼び出して各トライアドを他のコードと組み合わせて表示します。これにより、音楽理論に基づいたコードの組み合わせを視覚的に確認することができます。

このコードは、音楽理論を学ぶためのツールとして使用でき、異なるコードの組み合わせがどのように音楽的に響くかを理解するのに役立ちます。

## 期待される結果

```Python
C  +  C:
        C E G
C  +  Cm:
        C E Eb G
C  +  Cdim:
        C E Eb G Gb
C  +  Caug:
        Ab C E G
C  +  Csus4:
        C E F G
C  +  Csus2:
        C D E G
C  +  Db:
        Ab C Db E F G
C  +  Dbm:
        Ab C Db E G
C  +  Dbdim:
        C Db E G
C  +  Dbaug:
        A C Db E F G
C  +  Dbsus4:
        Ab C Db E G Gb
C  +  Dbsus2:
        Ab C Db E Eb G
C  +  D:
        A C D E F# G
C  +  Dm:
        A C D E F G
C  +  Ddim:
        C D E F G G#
C  +  Daug:
        A# C D E F# G
C  +  Dsus4:
        A C D E G
C  +  Dsus2:
        A C D E G
C  +  Eb:
        Bb C E Eb G
C  +  Ebm:
        Bb C E Eb G Gb
C  +  Ebdim:
        A C E Eb G Gb
C  +  Ebaug:
        B C E Eb G
C  +  Ebsus4:
        Ab Bb C E Eb G
C  +  Ebsus2:
        Bb C E Eb F G
C  +  E:
        B C E G G#
C  +  Em:
        B C E G
C  +  Edim:
        A# C E G
C  +  Eaug:
        C E G G#
C  +  Esus4:
        A B C E G
C  +  Esus2:
        B C E F# G
C  +  F:
        A C E F G
C  +  Fm:
        Ab C E F G
C  +  Fdim:
        Ab B C E F G
C  +  Faug:
        A C Db E F G
C  +  Fsus4:
        Bb C E F G
C  +  Fsus2:
        C E F G
C  +  Gb:
        Bb C Db E G Gb
C  +  Gbm:
        A C Db E G Gb
C  +  Gbdim:
        A C E G Gb
C  +  Gbaug:
        Bb C D E G Gb
C  +  Gbsus4:
        B C Db E G Gb
C  +  Gbsus2:
        Ab C Db E G Gb
C  +  G:
        B C D E G
C  +  Gm:
        A# C D E G
C  +  Gdim:
        A# C C# E G
C  +  Gaug:
        B C D# E G
C  +  Gsus4:
        C D E G
C  +  Gsus2:
        A C D E G
C  +  Ab:
        Ab C E Eb G
C  +  Abm:
        Ab B C E Eb G
C  +  Abdim:
        Ab B C D E G
C  +  Abaug:
        Ab C E G
C  +  Absus4:
        Ab C Db E Eb G
C  +  Absus2:
        Ab Bb C E Eb G
C  +  A:
        A C C# E G
C  +  Am:
        A C E G
C  +  Adim:
        A C D# E G
C  +  Aaug:
        A C C# E F G
C  +  Asus4:
        A C D E G
C  +  Asus2:
        A B C E G
C  +  Bb:
        Bb C D E F G
C  +  Bbm:
        Bb C Db E F G
C  +  Bbdim:
        Bb C Db E G
C  +  Bbaug:
        Bb C D E G Gb
C  +  Bbsus4:
        Bb C E Eb F G
C  +  Bbsus2:
        Bb C E F G
C  +  B:
        B C D# E F# G
C  +  Bm:
        B C D E F# G
C  +  Bdim:
        B C D E F G
C  +  Baug:
        B C D# E G
C  +  Bsus4:
        B C E F# G
C  +  Bsus2:
        B C C# E F# G
=====================================
Am  +  C:
        A C E G
Am  +  Cm:
        A C E Eb G
Am  +  Cdim:
        A C E Eb Gb
Am  +  Caug:
        A Ab C E
Am  +  Csus4:
        A C E F G
Am  +  Csus2:
        A C D E G
Am  +  Db:
        A Ab C Db E F
Am  +  Dbm:
        A Ab C Db E
Am  +  Dbdim:
        A C Db E G
Am  +  Dbaug:
        A C Db E F
Am  +  Dbsus4:
        A Ab C Db E Gb
Am  +  Dbsus2:
        A Ab C Db E Eb
Am  +  D:
        A C D E F#
Am  +  Dm:
        A C D E F
Am  +  Ddim:
        A C D E F G#
Am  +  Daug:
        A A# C D E F#
Am  +  Dsus4:
        A C D E G
Am  +  Dsus2:
        A C D E
Am  +  Eb:
        A Bb C E Eb G
Am  +  Ebm:
        A Bb C E Eb Gb
Am  +  Ebdim:
        A C E Eb Gb
Am  +  Ebaug:
        A B C E Eb G
Am  +  Ebsus4:
        A Ab Bb C E Eb
Am  +  Ebsus2:
        A Bb C E Eb F
Am  +  E:
        A B C E G#
Am  +  Em:
        A B C E G
Am  +  Edim:
        A A# C E G
Am  +  Eaug:
        A C E G#
Am  +  Esus4:
        A B C E
Am  +  Esus2:
        A B C E F#
Am  +  F:
        A C E F
Am  +  Fm:
        A Ab C E F
Am  +  Fdim:
        A Ab B C E F
Am  +  Faug:
        A C Db E F
Am  +  Fsus4:
        A Bb C E F
Am  +  Fsus2:
        A C E F G
Am  +  Gb:
        A Bb C Db E Gb
Am  +  Gbm:
        A C Db E Gb
Am  +  Gbdim:
        A C E Gb
Am  +  Gbaug:
        A Bb C D E Gb
Am  +  Gbsus4:
        A B C Db E Gb
Am  +  Gbsus2:
        A Ab C Db E Gb
Am  +  G:
        A B C D E G
Am  +  Gm:
        A A# C D E G
Am  +  Gdim:
        A A# C C# E G
Am  +  Gaug:
        A B C D# E G
Am  +  Gsus4:
        A C D E G
Am  +  Gsus2:
        A C D E G
Am  +  Ab:
        A Ab C E Eb
Am  +  Abm:
        A Ab B C E Eb
Am  +  Abdim:
        A Ab B C D E
Am  +  Abaug:
        A Ab C E
Am  +  Absus4:
        A Ab C Db E Eb
Am  +  Absus2:
        A Ab Bb C E Eb
Am  +  A:
        A C C# E
Am  +  Am:
        A C E
Am  +  Adim:
        A C D# E
Am  +  Aaug:
        A C C# E F
Am  +  Asus4:
        A C D E
Am  +  Asus2:
        A B C E
Am  +  Bb:
        A Bb C D E F
Am  +  Bbm:
        A Bb C Db E F
Am  +  Bbdim:
        A Bb C Db E
Am  +  Bbaug:
        A Bb C D E Gb
Am  +  Bbsus4:
        A Bb C E Eb F
Am  +  Bbsus2:
        A Bb C E F
Am  +  B:
        A B C D# E F#
Am  +  Bm:
        A B C D E F#
Am  +  Bdim:
        A B C D E F
Am  +  Baug:
        A B C D# E G
Am  +  Bsus4:
        A B C E F#
Am  +  Bsus2:
        A B C C# E F#
=====================================
G  +  C:
        B C D E G
G  +  Cm:
        B C D Eb G
G  +  Cdim:
        B C D Eb G Gb
G  +  Caug:
        Ab B C D E G
G  +  Csus4:
        B C D F G
G  +  Csus2:
        B C D G
G  +  Db:
        Ab B D Db F G
G  +  Dbm:
        Ab B D Db E G
G  +  Dbdim:
        B D Db E G
G  +  Dbaug:
        A B D Db F G
G  +  Dbsus4:
        Ab B D Db G Gb
G  +  Dbsus2:
        Ab B D Db Eb G
G  +  D:
        A B D F# G
G  +  Dm:
        A B D F G
G  +  Ddim:
        B D F G G#
G  +  Daug:
        A# B D F# G
G  +  Dsus4:
        A B D G
G  +  Dsus2:
        A B D E G
G  +  Eb:
        B Bb D Eb G
G  +  Ebm:
        B Bb D Eb G Gb
G  +  Ebdim:
        A B D Eb G Gb
G  +  Ebaug:
        B D Eb G
G  +  Ebsus4:
        Ab B Bb D Eb G
G  +  Ebsus2:
        B Bb D Eb F G
G  +  E:
        B D E G G#
G  +  Em:
        B D E G
G  +  Edim:
        A# B D E G
G  +  Eaug:
        B C D E G G#
G  +  Esus4:
        A B D E G
G  +  Esus2:
        B D E F# G
G  +  F:
        A B C D F G
G  +  Fm:
        Ab B C D F G
G  +  Fdim:
        Ab B D F G
G  +  Faug:
        A B D Db F G
G  +  Fsus4:
        B Bb C D F G
G  +  Fsus2:
        B C D F G
G  +  Gb:
        B Bb D Db G Gb
G  +  Gbm:
        A B D Db G Gb
G  +  Gbdim:
        A B C D G Gb
G  +  Gbaug:
        B Bb D G Gb
G  +  Gbsus4:
        B D Db G Gb
G  +  Gbsus2:
        Ab B D Db G Gb
G  +  G:
        B D G
G  +  Gm:
        A# B D G
G  +  Gdim:
        A# B C# D G
G  +  Gaug:
        B D D# G
G  +  Gsus4:
        B C D G
G  +  Gsus2:
        A B D G
G  +  Ab:
        Ab B C D Eb G
G  +  Abm:
        Ab B D Eb G
G  +  Abdim:
        Ab B D G
G  +  Abaug:
        Ab B C D E G
G  +  Absus4:
        Ab B D Db Eb G
G  +  Absus2:
        Ab B Bb D Eb G
G  +  A:
        A B C# D E G
G  +  Am:
        A B C D E G
G  +  Adim:
        A B C D D# G
G  +  Aaug:
        A B C# D F G
G  +  Asus4:
        A B D E G
G  +  Asus2:
        A B D E G
G  +  Bb:
        B Bb D F G
G  +  Bbm:
        B Bb D Db F G
G  +  Bbdim:
        B Bb D Db E G
G  +  Bbaug:
        B Bb D G Gb
G  +  Bbsus4:
        B Bb D Eb F G
G  +  Bbsus2:
        B Bb C D F G
G  +  B:
        B D D# F# G
G  +  Bm:
        B D F# G
G  +  Bdim:
        B D F G
G  +  Baug:
        B D D# G
G  +  Bsus4:
        B D E F# G
G  +  Bsus2:
        B C# D F# G
=====================================
```
