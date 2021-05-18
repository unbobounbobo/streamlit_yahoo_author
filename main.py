import streamlit as st
import pandas as pd
import altair as alt


st.title("ヤフーオーサー分析")

st.write("全オーサー：577名　データ更新：2021/4/25　※カテゴリーが複数にまたがるオーサーは独自に分類しています")

df = pd.read_csv("20210518_yahoo_outher2_重複整理済.csv", encoding='cp932')

st.write(df)

# 全体グラフ
c = alt.Chart(df).mark_circle(size=100).encode(
    x='記事数', y='コメント数', color='カテゴリー', size="Twitterフォロワー数",
    tooltip=["名前","職業","プロフィール",'記事数', 'コメント数', 'カテゴリー', "Twitterフォロワー数","Twitterフォロー数","Twitter投稿数","Twitterリスト数","TwitterF/F比"]).interactive()
st.altair_chart(c, use_container_width=True)

bar = df["カテゴリー"].value_counts(sort=True,ascending=True)
st.bar_chart(bar, use_container_width=True)

# 名前絞り込み
selected_name = st.multiselect(
    "オーサー名を絞り込んで表示する",
    df["名前"]
    )
df2 = df[df["名前"].isin(selected_name)]

name_c = alt.Chart(df2).mark_circle(size=300).encode(
    x='記事数', y='コメント数', color='カテゴリー', size="Twitterフォロワー数",
    tooltip=["名前","職業","プロフィール",'記事数', 'コメント数', 'カテゴリー', "Twitterフォロワー数"])

st.altair_chart(name_c, use_container_width=True)

# カテゴリー絞り込み
selected_cate = st.multiselect(
    "カテゴリーを絞り込んで表示する",
    df["カテゴリー"].unique()
    )
df3 = df[df["カテゴリー"].isin(selected_cate)]

cate_c = alt.Chart(df3).mark_circle(size=300).encode(
    x='記事数', y='コメント数', color='カテゴリー', size="Twitterフォロワー数",
    tooltip=["名前","職業","プロフィール",'記事数', 'コメント数', 'カテゴリー', "Twitterフォロワー数"]).interactive()

st.altair_chart(cate_c, use_container_width=True)


# プロフィールから絞り込み
input_text = st.text_input(
    "プロフィールや職業からテキストで検索する",
    "ワクチン"
    )
selected_bio = []

selected_bio.append(input_text)

df4 = df[df["プロフィール"].str.contains(selected_bio[0]) | df["名前"].str.contains(selected_bio[0])]

st.write(df4)

bio_c = alt.Chart(df4).mark_circle(size=300).encode(
    x='記事数', y='コメント数', color='カテゴリー', size="Twitterフォロワー数",
    tooltip=["名前","職業","プロフィール",'記事数', 'コメント数', 'カテゴリー', "Twitterフォロワー数"]).interactive()


st.altair_chart(bio_c, use_container_width=True)
